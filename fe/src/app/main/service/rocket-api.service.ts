import {Injectable} from '@angular/core';
import {HttpClient} from "@angular/common/http";
import {Observable} from "rxjs";
import {RocketNodeModel, RocketPropertyModel} from "../models/rocket.modell";
import {environment} from "../../../environments/environment";

@Injectable({
  providedIn: 'root'
})
export class RocketApiService {

  constructor(private http: HttpClient) {}

  public getTree(path: string): Observable<RocketNodeModel> {
    const url = `${environment.host}:${environment.port}/api/rocket/construction/${path}`;
    return this.http.get<RocketNodeModel>(url);
  }

  public createNode(path: string, rocketProperty?: RocketPropertyModel): Observable<RocketNodeModel> {
    const url = `${environment.host}:${environment.port}/api/rocket/construction/${path}`;
    return this.http.post<RocketNodeModel>(url, rocketProperty);
  }

  public deleteNode(nodeId: number): Observable<boolean> {
    const url = `${environment.host}:${environment.port}/api/rocket/node/${nodeId}`;
    return this.http.delete<boolean>(url);
  }

  public deleteProperty(propertyId: number): Observable<boolean> {
    const url = `${environment.host}:${environment.port}/api/rocket/property/${propertyId}`;
    return this.http.delete<boolean>(url);
  }
}
