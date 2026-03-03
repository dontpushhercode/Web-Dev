import { Component } from '@angular/core';
import { CommonModule } from '@angular/common'; 
import { ActivatedRoute, RouterLink } from '@angular/router';
import { AlbumService } from '../../services/album.service';
import { Observable, switchMap } from 'rxjs';
import { Photo } from '../photo.model';
import { AsyncPipe } from '@angular/common';

@Component({
  selector: 'app-album-photos-component',
  standalone: true,
  imports: [CommonModule, AsyncPipe, RouterLink],
  templateUrl: './album-photos-component.html',
  styleUrls: ['./album-photos-component.css'],
})
export class AlbumPhotosComponent {
  albumId!: number;
  photos$!: Observable<Photo[]>;

  constructor(private route: ActivatedRoute, private albumService: AlbumService) {}

  ngOnInit() {
    this.photos$ = this.route.paramMap.pipe(
      switchMap(params => {
        this.albumId = Number(params.get('id'));
        return this.albumService.getPhotos(this.albumId);
      })
    );
  }

  trackByPhotoId(index: number, photo: Photo) {
    return photo.id;
  }
}
