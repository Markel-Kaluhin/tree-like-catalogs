import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ConfirmationModalComponent } from './confirmation-modal.component';

describe('ConfirmationComponent', () => {
  let component: ConfirmationModalComponent;
  let fixture: ComponentFixture<ConfirmationModalComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [ConfirmationModalComponent]
    });
    fixture = TestBed.createComponent(ConfirmationModalComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
