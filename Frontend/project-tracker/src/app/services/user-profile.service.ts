import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class UserProfileService {
  api_link: string = "http://localhost:8000/";
  constructor(private http: HttpClient) { }

  // findOne(id: number): Observable<any> {
  //   return this.http.get('/api/users/' + id).pipe(
  //     map((user:any) => user)
  //   )
  // }

  getStudent(id: string): Observable<any> {
    return this.http.get(this.api_link + 'auth/api/students/' + id);
  }
}