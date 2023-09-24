export interface NonFlatAttrsPropertyModel {
  id: number;
  name: string;
  value: number;
  createdAt: Date;
}

export interface NonFlatAttrsNodeModel {
  id?: number;
  parentId: number;
  name: string;
  children: NonFlatAttrsNodeModel[];
  parent: any;
  properties: NonFlatAttrsPropertyModel[];
  createdAt: Date;
}
