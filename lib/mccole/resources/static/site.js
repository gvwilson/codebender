/**
 * Find and fix bibliographic citations.
 * @param {string} toRoot Path to root of site.
 */
const fixCites = (toRoot) => {
  Array.from(document.querySelectorAll('cite'))
    .forEach(node => {
      const keys = node.innerHTML
            .split(',')
            .map(key => key.trim())
            .map(key => `<a href="${toRoot}/bibliography/#${key}">${key}</a>`)
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
const fixPage = (toRoot='.') => {
  fixCites(toRoot)
}
