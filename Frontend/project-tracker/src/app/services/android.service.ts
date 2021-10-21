import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn: 'root'
})

export class AndroidService{
    api_link: string = "http://localhost:8000/";
    constructor( private http: HttpClient) { }

    getAndroidProjects(){
        return this.http.get(this.api_link + 'auth/api/styles/1/projects');
    }
}