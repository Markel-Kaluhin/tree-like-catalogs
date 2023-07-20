import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { map, switchMap } from 'rxjs/operators';

import { RocketApiService } from '../service/rocket-api.service';
import * as RocketActions from './rocket.actions';

@Injectable()
export class RocketEffects {
  getUserById$ = createEffect(() =>
    this.actions$.pipe(
      ofType(RocketActions.getTree),
      switchMap((action) => this.service.getTree(action.path).pipe(map((data) => RocketActions.getTreeSuccess({ rocket: data }))))
    )
  );
  createUser$ = createEffect(() =>
    this.actions$.pipe(
      ofType(RocketActions.createNode),
      switchMap((action) => this.service.createNode(action.path, action.rocketProperty).pipe(map((data) => RocketActions.createNodeSuccess({ rocket: data }))))
    )
  );
  deleteNode$ = createEffect(() =>
    this.actions$.pipe(
      ofType(RocketActions.deleteNode),
      switchMap((action) => this.service.deleteNode(action.nodeId).pipe(map((data) => RocketActions.deleteNodeSuccess({ success: data }))))
    )
  );
  deleteProperty$ = createEffect(() =>
    this.actions$.pipe(
      ofType(RocketActions.deleteProperty),
      switchMap((action) => this.service.deleteProperty(action.propertyId).pipe(map((data) => RocketActions.deletePropertySuccess({ success: data }))))
    )
  );
  constructor(private actions$: Actions, private service: RocketApiService) {}
}
