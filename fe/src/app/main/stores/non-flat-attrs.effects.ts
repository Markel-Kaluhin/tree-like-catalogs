import { Injectable } from '@angular/core';
import { Actions, createEffect, ofType } from '@ngrx/effects';
import { map, switchMap } from 'rxjs/operators';

import { NonFlatAttrsApiService } from '../service/non-flat-attrs-api.service';
import * as NonFlatAttrsActions from './non-flat-attrs.actions';

@Injectable()
export class NonFlatAttrsEffects {
  getUserById$ = createEffect(() =>
    this.actions$.pipe(
      ofType(NonFlatAttrsActions.getTree),
      switchMap((action) =>
        this.service
          .getTree(action.path)
          .pipe(
            map((data) =>
              NonFlatAttrsActions.getTreeSuccess({ nonFlatAttrs: data }),
            ),
          ),
      ),
    ),
  );
  createUser$ = createEffect(() =>
    this.actions$.pipe(
      ofType(NonFlatAttrsActions.createNode),
      switchMap((action) =>
        this.service
          .createNode(action.path, action.nonFlatAttrsProperty)
          .pipe(
            map((data) =>
              NonFlatAttrsActions.createNodeSuccess({ nonFlatAttrs: data }),
            ),
          ),
      ),
    ),
  );
  deleteNode$ = createEffect(() =>
    this.actions$.pipe(
      ofType(NonFlatAttrsActions.deleteNode),
      switchMap((action) =>
        this.service
          .deleteNode(action.nodeId)
          .pipe(
            map((data) =>
              NonFlatAttrsActions.deleteNodeSuccess({ success: data }),
            ),
          ),
      ),
    ),
  );
  deleteProperty$ = createEffect(() =>
    this.actions$.pipe(
      ofType(NonFlatAttrsActions.deleteProperty),
      switchMap((action) =>
        this.service
          .deleteProperty(action.propertyId)
          .pipe(
            map((data) =>
              NonFlatAttrsActions.deletePropertySuccess({ success: data }),
            ),
          ),
      ),
    ),
  );
  constructor(
    private actions$: Actions,
    private service: NonFlatAttrsApiService,
  ) {}
}
