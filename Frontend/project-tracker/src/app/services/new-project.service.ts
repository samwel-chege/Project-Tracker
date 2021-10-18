import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class NewProjectService {
  api_link: string = "http://localhost:8000/";


  constructor(private http: HttpClient) { }

  addprojects(){
    return this.http.post<any>(this.api_link + 'auth/api/projects/new/',{body:'any'});
  }
}
