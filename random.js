function withQueryParams(baseUrl, params) {
    const paramsWithoutNullishValues = {};
    for (const [key, val] of Object.entries(params)) {
        if (val == null) {
            continue;
        }
        paramsWithoutNullishValues[key] = val;
    }
    return `${baseUrl}?${JSON.stringify(paramsWithoutNullishValues)}`;
}
console.log(withQueryParams("", ["test1", "test2"]));
