import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http'
import { API_URL } from '../env';
import { getLocaleDateFormat } from '@angular/common';
@Injectable({
  providedIn: 'root'
})
export class PhoneService {
  phones: JSON

  constructor(private httpClient: HttpClient) { }
  ngOnInit(): void {
    //Called after the constructor, initializing input properties, and the first call to ngOnChanges.
    //Add 'implements OnInit' to the class.

    }

    getData() {
      this.httpClient.get(`http://0.0.0.0:5000/phones`).subscribe(data => {
        this.phones = data as JSON;
        console.log(data)
    })
  }
}
