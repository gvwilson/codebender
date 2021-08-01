/**
 * Add slide logo.
 */
const addSlideLogo = () => {
  Array.from(document.querySelectorAll('.remark-slide-content'))
    .filter(node => !node.classList.contains('title-slide'))
    .forEach(el => {
      console.log('ADDING')
      el.innerHTML += '<div class="slides-logo"></div>'
    })
}

/**
 * Find and fix bibliographic citations.
 * @param {string} toRoot Path to root of site.
 */
const fixBibCites = (toRoot) => {
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
 * Find and fix glossary references.
 * @param {string} toRoot Path to root of site.
 */
const fixGlossRefs = (toRoot) => {
  Array.from(document.querySelectorAll('a'))
    .filter(node => node.getAttribute('href').startsWith('g#'))
    .forEach(node => {
      const key = node.getAttribute('href').replace('g#', '')
      node.setAttribute('href', `${toRoot}/glossary/#${key}`)
      node.classList.add('glossary')
    })
}

/**
 * Perform all in-page fixes.
 * @param {string} toRoot Path to root of site (default is one level up).
 */
const fixPage = (toRoot='..') => {
  addSlideLogo()
  fixBibCites(toRoot)
  fixGlossRefs(toRoot)
}
