window.FakeMoney = {}
window.FakeMoney.User = {
    get token() { return localStorage["API_TOKEN"];},
    set token(token) { localStorage["API_TOKEN"] = token;},
    data: {
        firstName: "Juan",
        middleName: "Jose",
        lastName_1: "Perez",
        lastName_2: "Hernandez",
        email: "user_a@ekiim.xyz",
        phone: "+5266412345678",
        get birthdate() {
            const d = new Date(1994,12,23)
            const ye = new Intl.DateTimeFormat('es', { year: 'numeric' }).format(d);
            const mo = new Intl.DateTimeFormat('es', { month: 'long' }).format(d);
            const da = new Intl.DateTimeFormat('es', { day: '2-digit' }).format(d);
            return (`${mo} ${da}, del ${ye}`);
        },
        picture: "/assets/avatar1.png"
    },
    transactions: [
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123},
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123},
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123},
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123}
    ]
}

        
