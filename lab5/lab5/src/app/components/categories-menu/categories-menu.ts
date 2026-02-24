import { Component, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-categories-menu',
  imports: [CommonModule],
  standalone: true,
  templateUrl: './categories-menu.html',
  styleUrl: './categories-menu.css',
})
export class CategoriesMenu {

  selectedCategory = 0;

  @Output() categoryChanged = new EventEmitter<number>();

  selectCategory(id: number) {
    this.selectedCategory = id;
    this.categoryChanged.emit(id);
  }
}
