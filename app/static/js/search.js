let search_div = document.querySelector(".search-result")

document.addEventListener("DOMContentLoaded", search());

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
    search_div.innerHTML = `<p>Произошла ошибка при поиске. ${response.status}</p>`
}

function err(error) {
    search_div.innerHTML = `<p>Произошла ошибка. ${error}</p>`
}

function search_results(json) {
    search_div.innerHTML = ""
    json.forEach(entry => {
        add_entry(entry)
        console.log(entry)
    });
}

function add_entry(entry) {
    let entry_div = 
    `<a href='/library/${entry[0]}'>
        <div class='entry'>
            <p class='entry-title'>${entry[1]}</p>
            <p>Автор: ${entry[2]}</p>
            <p>Год издания: ${entry[3]}</p>
            <p>${entry[4].substring(0, 127) + "..."}</p>
        </div>
    </a>`
    search_div.innerHTML += entry_div
}