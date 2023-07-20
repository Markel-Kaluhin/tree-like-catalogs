export interface RocketPropertyModel {
  id: number;
  name: string;
  value: number;
  createdAt: Date;
}

export interface RocketNodeModel {
  id?: number;
  parentId: number;
  name: string;
  children: RocketNodeModel[];
  parent: any;
  properties: RocketPropertyModel[];
  createdAt: Date;
}
