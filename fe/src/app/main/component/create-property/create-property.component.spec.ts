import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatePropertyComponent } from './create-property.component';

describe('CreatePropertyComponent', () => {
  let component: CreatePropertyComponent;
  let fixture: ComponentFixture<CreatePropertyComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreatePropertyComponent]
    });
    fixture = TestBed.createComponent(CreatePropertyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
