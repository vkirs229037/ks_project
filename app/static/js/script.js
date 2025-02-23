async function test() {
    const url = "/api/test";
    try {
        const response = await fetch(url);
        if (!response.ok) {
            throw new Error(`Response error: ${response.status}`)
        }

        const json = await response.json()
        console.log(json)
    }
    catch (error) {
        console.log(error)
    }
}