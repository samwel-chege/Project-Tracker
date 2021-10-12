import { Injectable } from "@angular/core";
import { HttpClient } from "@angular/common/http";
import { Observable } from "rxjs";

@Injectable()
export class ProjectService{
    constructor(private httpclient: HttpClient){ }

    // getprojects(): Observable<any>{
    //     return this.httpclient.get()
    // }
}