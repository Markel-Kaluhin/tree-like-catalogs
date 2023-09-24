import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {NonFlatAttrsNodeModel, NonFlatAttrsPropertyModel} from "../models/non-flat-attrs.modell";
import {environment} from "../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class NonFlatAttrsApiService {

  constructor(private http: HttpClient) {}

  public getTree(path: string): Observable<NonFlatAttrsNodeModel> {
    const url = `${environment.host}:${environment.port}/api/non_flat_attrs/construction/${path}`;
    return this.http.get<NonFlatAttrsNodeModel>(url);
  }

  public createNode(path: string, nonFlatAttrsProperty?: NonFlatAttrsPropertyModel): Observable<NonFlatAttrsNodeModel> {
    const url = `${environment.host}:${environment.port}/api/non_flat_attrs/construction/${path}`;
    return this.http.post<NonFlatAttrsNodeModel>(url, nonFlatAttrsProperty);
  }

  public deleteNode(nodeId: number): Observable<boolean> {
    const url = `${environment.host}:${environment.port}/api/non_flat_attrs/node/${nodeId}`;
    return this.http.delete<boolean>(url);
  }

  public deleteProperty(propertyId: number): Observable<boolean> {
    const url = `${environment.host}:${environment.port}/api/non_flat_attrs/property/${propertyId}`;
    return this.http.delete<boolean>(url);
  }
}
