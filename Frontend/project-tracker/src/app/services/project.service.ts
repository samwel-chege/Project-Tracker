import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { FormsModule } from "@angular/forms";
import { Observable } from "rxjs";

@Injectable({
    providedIn: 'root'
})

export class ProjectService{
    api_link: string = "https://taliban-trackerapp.herokuapp.com/";
    constructor( private http: HttpClient) { }

    getprojects(){
        return this.http.get(this.api_link + 'auth/api/projects/');
    }

}