import { Component } from '@angular/core';
import {UntypedFormBuilder, UntypedFormControl, UntypedFormGroup, Validators} from "@angular/forms";
import {NgbActiveOffcanvas} from "@ng-bootstrap/ng-bootstrap";

@Component({
  selector: 'app-create-property',
  templateUrl: './create-property.component.html',
  styleUrls: ['./create-property.component.scss']
})
export class CreatePropertyComponent {
  public rocketPropertyForm: UntypedFormGroup;

  constructor(
    private formBuilder: UntypedFormBuilder,
    public activeOffCanvas: NgbActiveOffcanvas,
  ) {}

  ngOnInit(): void {
    this.rocketPropertyForm = this.formBuilder.group({
      name: new UntypedFormControl('', [Validators.required]),
      value: new UntypedFormControl('', [Validators.required]),
    })
  }

  public save(){
    this.activeOffCanvas.close(
      this.rocketPropertyForm.value
    )
  }
}
