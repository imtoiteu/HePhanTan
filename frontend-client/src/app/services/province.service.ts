import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class ProvinceService {

  provinces = 'https://vnprovinces.pythonanywhere.com/api/provinces/'
  districts = 'https://vnprovinces.pythonanywhere.com/api/districts/';
  wards = 'https://vnprovinces.pythonanywhere.com/api/wards/';

  province = 'https://vnprovinces.pythonanywhere.com/api/provinces/';
  district = 'https://vnprovinces.pythonanywhere.com/api/districts/';  
  ward = 'https://vnprovinces.pythonanywhere.com/api/wards/';

  constructor(private http: HttpClient) { }

  getAllProvinces() {
    return this.http.get(this.provinces);
  }

  getDistricts(code:number) {
    return this.http.get(this.districts+'/'+code+'?depth=2');
  }

  getWards(code:number) {
    return this.http.get(this.wards+'/'+code+'?depth=2');
  }

  getProvince(id: number) {
    return this.http.get(this.province+id);
  }

  getDistrict(id: number) {
    return this.http.get(this.district+id);
  }

  getWard(id: number) {
    return this.http.get(this.ward+id);
  }
}
