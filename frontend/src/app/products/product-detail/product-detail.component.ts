import { Component, OnInit, ViewChild, ElementRef } from '@angular/core';
import { ActivatedRoute, Params } from '@angular/router';
import { CartService } from 'src/app/shared/service/cart.service';

@Component({
  selector: 'app-product-detail',
  templateUrl: './product-detail.component.html',
  styleUrls: ['./product-detail.component.css']
})
export class ProductDetailComponent implements OnInit {
  @ViewChild("quantity") quantity: ElementRef
  phoneInfo: PhoneInfo = {}
  name: string
  category: string
  constructor(private route: ActivatedRoute, private cartService: CartService) { }

  ngOnInit(): void {
    this.route.params.subscribe((params: Params) => {
      this.name = params['name'];
      this.category = params['category']
    })
  }


}

interface PhoneInfo {
  name?: string,
  category?: string,
  price?: number
}