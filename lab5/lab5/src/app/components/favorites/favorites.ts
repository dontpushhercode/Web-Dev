import { Component, Input } from '@angular/core';
import { CommonModule } from '@angular/common';
import { Product } from '../../models/product';
import { PRODUCTS } from '../../data/products';
import { ProductItem } from '../product-item/product-item';
import { ProductList } from '../product-list/product-list';

@Component({
  selector: 'app-favorites',
  standalone: true,
  imports: [CommonModule, ProductList],
  templateUrl: './favorites.html',
  styleUrls: ['./favorites.css']
})
export class Favorites {
  // allProducts: Product[] = PRODUCTS;
  @Input() allProducts: Product[] = [];

  isOpen = false

  toggle() {
    this.isOpen = !this.isOpen;
  }

  get favorites(): Product[] {
    return this.allProducts.filter(product => product.favorite);
  }

  removeProduct(productToRemove: Product) {
    const index = this.allProducts.findIndex(p => p.id === productToRemove.id);
    if (index !== -1) this.allProducts.splice(index, 1);
  }
}
