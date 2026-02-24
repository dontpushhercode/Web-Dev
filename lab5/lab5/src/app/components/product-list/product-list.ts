import { Component, Input, output } from '@angular/core';
import { Product } from '../../models/product';
import { ProductItem } from '../product-item/product-item';
import { CommonModule } from '@angular/common';
import { PRODUCTS } from '../../data/products';

@Component({
  selector: 'app-product-list',
  standalone: true,
  imports: [CommonModule, ProductItem],
  templateUrl: './product-list.html',
  styleUrls: ['./product-list.css']
})

export class ProductList {
  @Input() products: Product[] = [];
  // products: Product[] = PRODUCTS;

  @Input() searchText = '';
  @Input() categoryId = 0;

  deleteProduct = output<Product>();
  
  get filteredProducts() {
    const search = this.searchText.toLowerCase();

    return this.products.filter(p =>
    (this.categoryId === 0 || p.categoryId === this.categoryId) &&
    (!search || p.name.toLowerCase().includes(search))
  );
  }
}
