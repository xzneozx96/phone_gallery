import { Component, OnInit } from '@angular/core';
import { PhoneService } from '../shared/phone.service';

@Component({
  selector: 'app-products',
  templateUrl: './products.component.html',
  styleUrls: ['./products.component.css']
})
export class ProductsComponent implements OnInit {

  constructor(private phoneService: PhoneService) { }

  ngOnInit() {
    this.phoneService.getData()
  }
}
