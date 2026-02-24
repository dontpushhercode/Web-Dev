export class Product {
  id!: number;
  name!: string;
  price!: number;
  image!: string;
  description!: string;
  link!: string;
  likes!: number;
  categoryId!: number;
  rating?: number;
  reviews?: number;
  favorite?: boolean;

  installmentTerm = 6;

  get inInstallments(): number {
    return Math.round(this.price / this.installmentTerm);
  }
   
  constructor(init?: Partial<Product>) {
    Object.assign(this, init);
  }
}