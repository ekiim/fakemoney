console.warn("Loading FakeMoney module");
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
        {id: 21, description: "Transaction Concept", direction: "In", amount: 123},
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123},
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123},
        {id: 1, description: "Transaction Concept", direction: "In", amount: 123}
    ],
	accounts: [
		{ "Saldo_total": 2129.25, "Egresos del periodo": 2135.02, "Ingresos del periodo": 3215.13, "Cantidad de transacciones": 6, "Fecha de consulta": "10/4/21", "Periodo de consulta": 31 },
		{ "Saldo_total": 2129.25, "Egresos del periodo": 2135.02, "Ingresos del periodo": 3215.13, "Cantidad de transacciones": 6, "Fecha de consulta": "10/4/21", "Periodo de consulta": 31 },
		{ "Saldo_total": 2129.25, "Egresos del periodo": 2135.02, "Ingresos del periodo": 3215.13, "Cantidad de transacciones": 6, "Fecha de consulta": "10/4/21", "Periodo de consulta": 31 },
		{ "Saldo_total": 2129.25, "Egresos del periodo": 2135.02, "Ingresos del periodo": 3215.13, "Cantidad de transacciones": 6, "Fecha de consulta": "10/4/21", "Periodo de consulta": 31 },
	]
}
window.FakeMoney.API = {}

window.FakeMoney.API.call = async (path, payload, method) => {
    const server = localStorage["API_URL"] || "https://api.fakemoney.ekiim.xyz";
    const url = `${server}${path}`;
    const headers = { "Content-Type": "application/json" }
    if (localStorage["API_KEY"]) {
        headers["Authorization"] = `Bearer ${localStorage["API_KEY"]||""}`
    }
    const request_options = {
        method: method || "GET",
        mode: "cors",
        headers: headers
    }
    if (payload) {
        request_options.body = JSON.stringify(payload)
    }
    const response = await fetch(url, request_options);
    console.log(response);
    const body = await response.json();
    return { status: response.status, payload: body }
}
window.FakeMoney.API.Signup = async (userdata) => {
    console.log(userdata);
    const {status, payload} = await window.FakeMoney.API.call(
        "/auth/signup", userdata, "POST"
    )
    if (status !== 201) {
        console.warn("Sign Up Error")
        console.warn(payload.message)
        return false
    }
    console.log("Sign Up succesful");
    return true
}
window.FakeMoney.API.Login = async (userdata) => {
    const {status, payload} = await window.FakeMoney.API.call(
        "/auth/login", userdata, "POST"
    )
    if (status !== 200) {
        console.warn("Auth Error")
        console.warn(payload.message)
        return false;
    }
    console.log("Login succesful");
    localStorage["API_KEY"] = payload.token;
    console.log(payload.token)
    return true;
}
window.FakeMoney.API.ValidateToken = async () => {
    const {status, payload} = await window.FakeMoney.API.call(
        "/auth/validate"
    )
    return status === 200
}
window.FakeMoney.test = {}
window.FakeMoney.test.data = {
    users: [
        {
            email: "test@test.com",
            phone: "+526641234567",
            password: "12345",
            password_confirmation: "12345",
            personal_data: {
                first_name: "Jose",
                last_name_1: "jose",
                birthdate: "1947-02-17"
            }

        }
    ]
}
window.FakeMoney.test.cases = {
    signup: [
    async () => {
        console.log("Signing Up user:")
        const user = window.FakeMoney.test.data.users[0];
        console.log(user)
        const signup_response = await window.FakeMoney.API.Signup(user);
        console.log(signup_response);
    },
    ]
}


window.FakeMoney.Client = {};
window.FakeMoney.Client.AuthOnly = () => {
    window.FakeMoney.API.ValidateToken().then((valid) => {
    if (!valid){
        console.log("Invalid Auth");
        window.location.href = "/login.html";
    }
    else { console.log("Valid Auth") }
    }).catch((e) => {
        console.log("Invalid Auth");
        window.location.href = "/login.html";
    })
}
