import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable({
    providedIn: 'root'
})

export class HomeService{
    api_link: string = "https://taliban-trackerapp.herokuapp.com/";
    constructor( private http: HttpClient) { }

    getprofiles(){
        return this.http.get(this.api_link + 'auth/api/students/');
    }
}