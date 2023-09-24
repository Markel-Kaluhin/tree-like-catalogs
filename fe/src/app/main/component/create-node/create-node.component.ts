import {Component, OnInit} from '@angular/core';
import {UntypedFormBuilder, UntypedFormControl, UntypedFormGroup, Validators} from "@angular/forms";
import {NgbActiveOffcanvas} from "@ng-bootstrap/ng-bootstrap";

@Component({
  selector: 'app-create-node',
  templateUrl: './create-node.component.html',
  styleUrls: ['./create-node.component.scss']
})
export class CreateNodeComponent implements OnInit {

  public nonFlatAttrsNodeForm: UntypedFormGroup;

  constructor(
    private formBuilder: UntypedFormBuilder,
    public activeOffCanvas: NgbActiveOffcanvas
  ) {}

  ngOnInit(): void {
    this.nonFlatAttrsNodeForm = this.formBuilder.group({
      name: new UntypedFormControl('', [Validators.required]),
    })
  }

  public save() {
    this.activeOffCanvas.close(
      this.nonFlatAttrsNodeForm.value
    )
  }

}
