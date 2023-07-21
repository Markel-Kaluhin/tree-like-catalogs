import { Component } from '@angular/core';
import {RocketService} from "../../service/rocket.service";
import {RocketNodeModel} from "../../models/rocket.modell";
import {Store} from "@ngrx/store";
import * as RocketSelector from '../../stores/rocket.selectors'
import * as RocketAction from '../../stores/rocket.actions'
import {NgbModal, NgbOffcanvas} from "@ng-bootstrap/ng-bootstrap";
import {ConfirmationModalComponent} from "../../../shared/component/confirmation/confirmation-modal.component";
import {CreateNodeComponent} from "../create-node/create-node.component";
import {CreatePropertyComponent} from "../create-property/create-property.component";
import {RelativeTimePipe} from "../../../shared/pipe/relative-time.pipe";

@Component({
  selector: 'app-root',
  templateUrl: './main.component.html',
  styleUrls: ['./main.component.scss'],
  providers: [RelativeTimePipe]
})
export class MainComponent {
  public root: RocketNodeModel[] = []
  public isOnRootLevel: boolean = true;
  private initialPath: string = 'Rocket'


  constructor(
    private rocketService: RocketService,
    private rocketStore: Store<RocketNodeModel>,
    private modalService: NgbModal,
    private offCanvasService: NgbOffcanvas,
  ) {
    this.rocketStore.dispatch(RocketAction.getTree({ path: this.initialPath }));
    this.subscribeToRocketStore();
  }

  private subscribeToRocketStore() {
    this.rocketStore
      .select(RocketSelector.rocketNode)
      .subscribe(rocket => {
        this.isOnRootLevel = rocket.name === this.initialPath
        this.root = [rocket]
      })
  }

  public createProperty(nodeId: number) {
    const offCanvasInstance = this.offCanvasService.open(CreatePropertyComponent, { position: 'end' });
    offCanvasInstance.result.then(
        (result) => {
          let path = this.getPathByNodeId(this.root[0], nodeId)
          path.reverse()
          path = path.join('/')
          this.rocketStore.dispatch(RocketAction.createNode({ path: path, rocketProperty: result }))
        },
        (reason) => {},
    )
  }

  public createChildNode(nodeId: number) {
    const offCanvasInstance = this.offCanvasService.open(CreateNodeComponent, { position: 'end' });
    offCanvasInstance.result.then(
        (result) => {
          let path = this.getPathByNodeId(this.root[0], nodeId)
          path.reverse()
          path.push(result.name)
          path = path.join('/')
          this.rocketStore.dispatch(RocketAction.createNode({ path: path }))
        },
        (reason) => {},
    )
  }

  public goToTop() {
    this.rocketStore.dispatch(RocketAction.getTree({ path: this.initialPath }));
  }

  public goToChildNode(nodeId: number) {
    let path = this.getPathByNodeId(this.root[0], nodeId)
    path = path.reverse().join('/')
    this.rocketStore.dispatch(RocketAction.getTree({ path: path }));
  }

  public deleteNode(nodeId: number, name: string) {
    const modalInstance = this.modalService.open(ConfirmationModalComponent)
    modalInstance.componentInstance.operation = 'delete'
    modalInstance.componentInstance.name = name
    modalInstance.componentInstance.type = 'node'
    modalInstance.result.then(
        (result) => {
          if (result) {
            this.rocketStore.dispatch(RocketAction.deleteNode({ nodeId: nodeId }))
            this.rocketStore.dispatch(RocketAction.getTree({ path: this.initialPath }));
          }},
        (reason) => {},
    )
  }

  public deleteProperty(propertyId: number, name: string) {
    const modalInstance = this.modalService.open(ConfirmationModalComponent)
    modalInstance.componentInstance.operation = 'delete'
    modalInstance.componentInstance.name = name
    modalInstance.componentInstance.type = 'property'
    modalInstance.result.then(
        (result) => {
          if (result) {
            this.rocketStore.dispatch(RocketAction.deleteProperty({ propertyId: propertyId }));
            this.rocketStore.dispatch(RocketAction.getTree({ path: this.initialPath }));
          }},
        (reason) => {},
    )
  }

  private getPathByNodeId(node: RocketNodeModel, matchNodeId: number, result: string[] = []): any {
    if (node?.id === matchNodeId) {
      result.push(node.name)
      matchNodeId = node.parentId
      return this.getPathByNodeId(node.parent, matchNodeId, result)
    } else {
      for (const child of node?.children || []) {
        const childNode = {...child, parent: node}
        this.getPathByNodeId(childNode, matchNodeId, result)
      }
    }
    return result
  }
}
