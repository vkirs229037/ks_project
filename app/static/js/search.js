async function search() {
    let title = document.querySelector("#search-title").value
    let author = document.querySelector("#search-author").value
    let year = document.querySelector("#search-year").value
    let desc = document.querySelector("#search-desc").value

    let url = "/api/search?" + new URLSearchParams({title: title, author: author, year: year, desc: desc})
    try {
        const response = await fetch(url);
        if (!response.ok) {
            search_err(response)
        }

        const json = await response.json()
        search_results(json)
    }
    catch (error) {
        console.log(error)
        err(error)
    }
}

function search_err(response) {
    let search_div = document.querySelector(".search-result")
    search_div.innerHTML = `<p>Произошла ошибка при поиске. ${response.status}</p>`
}

function err(error) {
    let search_div = document.querySelector(".search-result")
    search_div.innerHTML = `<p>Произошла ошибка. ${error}</p>`
}

function search_results(json) {
    let search_div = document.querySelector(".search-result")
    search_div.innerHTML = json
}