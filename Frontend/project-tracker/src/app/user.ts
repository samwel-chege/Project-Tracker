export class User {
    constructor(
        _id: string,
        name: string,
        email: string,
        public password: string,
        public username: string,
        // public email: string,
        public is_active: boolean,
        public is_staff: boolean,
        public created_at: Date,
        public updated_at: Date,
        public token: string,


    ){}
}
