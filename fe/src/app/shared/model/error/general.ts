import { HttpHeaders } from '@angular/common/http';

export interface ErrorDetail {
  detail: string;
}

export interface GeneralError {
  headers: HttpHeaders;
  status: number;
  statusText: string;
  ok: boolean;
  name: string;
  error: ErrorDetail;
}
