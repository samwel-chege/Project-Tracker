import { Injectable } from '@angular/core';
import { HttpClient, HttpParams } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { map, catchError } from 'rxjs/operators';


@Injectable({
  providedIn: 'root'
})
export class CohortService {
  api_link: string = "http://localhost:8000/";
  constructor(private http: HttpClient) { }

  getCohort(id: string): Observable<any> {
    return this.http.get(this.api_link + 'auth/api/cohorts/' + id + '/projects');
  }
}