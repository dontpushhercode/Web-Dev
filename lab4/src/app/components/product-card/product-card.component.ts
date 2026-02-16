import { CommonModule } from '@angular/common';
import { Component, EventEmitter, Input, Output, OnInit } from '@angular/core';
import { Product } from '../../models/product.model';

type SharePlatform = 'telegram' | 'whatsapp';

@Component({
  selector: 'app-product-card',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './product-card.component.html',
  styleUrl: './product-card.component.css'
})
export class ProductCardComponent implements OnInit {
  @Input() product!: Product;
  @Output() shared = new EventEmitter<{ productId: number; platform: SharePlatform }>();

  selectedImage = '';

  ngOnInit(): void {
    this.selectedImage = this.product.image;
  }

  setImage(img: string): void {
    this.selectedImage = img;
  }

  stars(): number[] {
    return [1, 2, 3, 4, 5];
  }

  
  fullStars(): number {
    return Math.floor(this.product.rating);
  }
}
