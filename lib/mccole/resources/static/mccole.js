/**
 * Find and fix bibliographic citations.
 * @param {string} bibPath Path to bibliography.
 */
const fixCites = (bibPath) => {
  Array.from(document.querySelectorAll('cite'))
    .forEach(node => {
      const keys = node.innerHTML
            .split(',')
            .map(key => key.trim())
            .map(key => `<a href="${bibPath}#${key}">${key}</a>`)
            .join(', ')
      const cite = document.createElement('span')
      cite.innerHTML = `[${keys}]`
      cite.classList.add('cite')
      node.parentNode.replaceChild(cite, node)
    })
}

/**
 * Perform all in-page fixes.
 * @param {string} toRoot Path to root of site (default is one level up).
 */
const fixPage = (bibPath) => {
  fixCites(bibPath)
}
