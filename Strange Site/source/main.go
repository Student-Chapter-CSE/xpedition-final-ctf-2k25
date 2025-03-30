package main

import (
	"fmt"
	"html/template"
	"log"
	"net/http"
)

const (
	PASSWORD = "gnosis{n33d_70_f1nd_d0c70r_57r4n63}"
)

func main() {
	fs := http.FileServer(http.Dir("static"))
	http.Handle("/static/", http.StripPrefix("/static/", fs))

	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		tmpl := template.Must(template.ParseFiles("templates/index.html"))
		tmpl.Execute(w, nil)
	})

	http.HandleFunc("/get-password", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprint(w, PASSWORD)
	})

	http.HandleFunc("/check-password", func(w http.ResponseWriter, r *http.Request) {
		if r.Method != http.MethodPost {
			http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
			return
		}

		inputPass := r.FormValue("password")

		if inputPass == PASSWORD {
			fmt.Fprint(w, "Correct! You've cracked the password!")
		} else {
			fmt.Fprint(w, "Wrong password, try again.")
		}
	})

	log.Println("Server starting on http://localhost:8080")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
