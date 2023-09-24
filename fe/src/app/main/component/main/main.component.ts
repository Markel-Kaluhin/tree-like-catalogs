import { Component } from '@angular/core';
import { NonFlatAttrsService } from '../../service/non-flat-attrs.service';
import { NonFlatAttrsNodeModel } from '../../models/non-flat-attrs.modell';
import { Store } from '@ngrx/store';
import * as NonFlatAttrsSelector from '../../stores/non-flat-attrs.selectors';
import * as NonFlatAttrsAction from '../../stores/non-flat-attrs.actions';
import { NgbModal, NgbOffcanvas } from '@ng-bootstrap/ng-bootstrap';
import { ConfirmationModalComponent } from '../../../shared/component/confirmation/confirmation-modal.component';
import { CreateNodeComponent } from '../create-node/create-node.component';
import { CreatePropertyComponent } from '../create-property/create-property.component';
import { RelativeTimePipe } from '../../../shared/pipe/relative-time.pipe';

@Component({
  selector: 'app-root',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss'],
  providers: [RelativeTimePipe],
})
export class MainComponent {
  public root: NonFlatAttrsNodeModel[] = [];
  public isOnRootLevel: boolean = true;
  private initialPath: string = 'ICE';

  constructor(
    private nonFlatAttrsService: NonFlatAttrsService,
    private nonFlatAttrsStore: Store<NonFlatAttrsNodeModel>,
    private modalService: NgbModal,
    private offCanvasService: NgbOffcanvas,
  ) {
    this.nonFlatAttrsStore.dispatch(
      NonFlatAttrsAction.getTree({ path: this.initialPath }),
    );
    this.subscribeToNonFlatAttrsStore();
  }

  private subscribeToNonFlatAttrsStore() {
    this.nonFlatAttrsStore
      .select(NonFlatAttrsSelector.nonFlatAttrsNode)
      .subscribe((nonFlatAttrs) => {
        this.isOnRootLevel = nonFlatAttrs.name === this.initialPath;
        this.root = [nonFlatAttrs];
      });
  }

  public createProperty(nodeId: number) {
    const offCanvasInstance = this.offCanvasService.open(
      CreatePropertyComponent,
      { position: 'end' },
    );
    offCanvasInstance.result.then(
      (result) => {
        let path = this.getPathByNodeId(this.root[0], nodeId);
        path.reverse();
        path = path.join('/');
        this.nonFlatAttrsStore.dispatch(
          NonFlatAttrsAction.createNode({
            path: path,
            nonFlatAttrsProperty: result,
          }),
        );
      },
      (reason) => {},
    );
  }

  public createChildNode(nodeId: number) {
    const offCanvasInstance = this.offCanvasService.open(CreateNodeComponent, {
      position: 'end',
    });
    offCanvasInstance.result.then(
      (result) => {
        let path = this.getPathByNodeId(this.root[0], nodeId);
        path.reverse();
        path.push(result.name);
        path = path.join('/');
        this.nonFlatAttrsStore.dispatch(
          NonFlatAttrsAction.createNode({ path: path }),
        );
      },
      (reason) => {},
    );
  }

  public goToTop() {
    this.nonFlatAttrsStore.dispatch(
      NonFlatAttrsAction.getTree({ path: this.initialPath }),
    );
  }

  public goToChildNode(nodeId: number) {
    let path = this.getPathByNodeId(this.root[0], nodeId);
    path = path.reverse().join('/');
    this.nonFlatAttrsStore.dispatch(NonFlatAttrsAction.getTree({ path: path }));
  }

  public deleteNode(nodeId: number, name: string) {
    const modalInstance = this.modalService.open(ConfirmationModalComponent);
    modalInstance.componentInstance.operation = 'delete';
    modalInstance.componentInstance.name = name;
    modalInstance.componentInstance.type = 'node';
    modalInstance.result.then(
      (result) => {
        if (result) {
          this.nonFlatAttrsStore.dispatch(
            NonFlatAttrsAction.deleteNode({ nodeId: nodeId }),
          );
          this.nonFlatAttrsStore.dispatch(
            NonFlatAttrsAction.getTree({ path: this.initialPath }),
          );
        }
      },
      (reason) => {},
    );
  }

  public deleteProperty(propertyId: number, name: string) {
    const modalInstance = this.modalService.open(ConfirmationModalComponent);
    modalInstance.componentInstance.operation = 'delete';
    modalInstance.componentInstance.name = name;
    modalInstance.componentInstance.type = 'property';
    modalInstance.result.then(
      (result) => {
        if (result) {
          this.nonFlatAttrsStore.dispatch(
            NonFlatAttrsAction.deleteProperty({ propertyId: propertyId }),
          );
          this.nonFlatAttrsStore.dispatch(
            NonFlatAttrsAction.getTree({ path: this.initialPath }),
          );
        }
      },
      (reason) => {},
    );
  }

  private getPathByNodeId(
    node: NonFlatAttrsNodeModel,
    matchNodeId: number,
    result: string[] = [],
  ): any {
    if (node?.id === matchNodeId) {
      result.push(node.name);
      matchNodeId = node.parentId;
      return this.getPathByNodeId(node.parent, matchNodeId, result);
    } else {
      for (const child of node?.children || []) {
        const childNode = { ...child, parent: node };
        this.getPathByNodeId(childNode, matchNodeId, result);
      }
    }
    return result;
  }
}
