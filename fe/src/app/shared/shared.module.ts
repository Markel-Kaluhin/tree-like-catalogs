import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ConfirmationModalComponent } from './component/confirmation/confirmation-modal.component';
import { RelativeTimePipe } from './pipe/relative-time.pipe';

@NgModule({
  declarations: [ConfirmationModalComponent, RelativeTimePipe],
  imports: [CommonModule],
  exports: [RelativeTimePipe],
})
export class SharedModule {}
