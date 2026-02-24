import { Component, Input, output } from '@angular/core';
import { Product } from '../../models/product';
import { CommonModule } from '@angular/common';
import { EventEmitter } from 'node:stream';

@Component({
  selector: 'app-product-item',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-item.html',
  styleUrl: './product-item.css',
})
export class ProductItem {
  @Input() product!: Product;

  deleteProduct = output<Product>();

  shareToWhatsApp() {
    const text = encodeURIComponent(
      `Check out this product: ${this.product.link}`
    );

    const url = `https://wa.me/?text=${text}`;
    window.open(url, '_blank');
  }

  shareToTelegram() {
    const link = encodeURIComponent(this.product.link);
    const name = encodeURIComponent(this.product.name);

    const url = `https://t.me/share/url?url=${link}&text=${name}`;
    window.open(url, '_blank');
  }

  toggleFavorite() {
    this.product.favorite = !this.product.favorite;
    
    this.product.likes += this.product.favorite ? 1 : -1;

    if (this.product.likes < 0) {
      this.product.likes = 0;
    }
  }

  remove() {
    this.deleteProduct.emit(this.product);
  }
}

