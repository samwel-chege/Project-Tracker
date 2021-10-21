import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";
import { map } from 'rxjs/operators';
import { catchError } from 'rxjs/internal/operators';

@Injectable({
  providedIn: "root",
})

export class SingleProjectService {
    api_link: string = "https://taliban-trackerapp.herokuapp.com/";
    constructor( private http: HttpClient) { }

    getProject(id: string): Observable<any> {
        return this.http.get(this.api_link + 'auth/api/projects/' + id);
    }
}