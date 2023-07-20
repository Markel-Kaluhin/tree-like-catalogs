import {Component, Input} from '@angular/core';
import {NgbActiveModal} from "@ng-bootstrap/ng-bootstrap";

@Component({
  selector: 'app-confirmation',
  // standalone: true,
  templateUrl: './confirmation-modal.component.html',
  styleUrls: ['./confirmation-modal.component.scss']
})
export class ConfirmationModalComponent {
  @Input() operation: string = '';
  @Input() name: string = '';
  @Input() type: string = '';

  constructor(public activeModal: NgbActiveModal) {}
}
