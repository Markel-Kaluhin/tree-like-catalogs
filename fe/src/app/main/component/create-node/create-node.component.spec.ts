import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreateNodeComponent } from './create-node.component';

describe('CreateNodeComponent', () => {
  let component: CreateNodeComponent;
  let fixture: ComponentFixture<CreateNodeComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      declarations: [CreateNodeComponent]
    });
    fixture = TestBed.createComponent(CreateNodeComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
