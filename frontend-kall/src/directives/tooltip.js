// src/directives/tooltip.js
import { Tooltip } from 'bootstrap'

export default {
  mounted(el, binding) {
    const value = typeof binding.value === 'string' ? { text: binding.value } : binding.value

    el.setAttribute('data-bs-toggle', 'tooltip')
    el.setAttribute('title', value.text || '')

    if (value.customClass) {
      el.setAttribute('data-bs-custom-class', value.customClass)
    }

    if (value.placement) {
      el.setAttribute('data-bs-placement', value.placement)
    }

    // Inicializar tooltip
    el._tooltip = new Tooltip(el, {
      trigger: value.trigger || 'hover focus',
      customClass: value.customClass || null,
      placement: value.placement || 'top',
    })
  },

  updated(el, binding) {
    const value = typeof binding.value === 'string' ? { text: binding.value } : binding.value
    if (el._tooltip) {
      el.setAttribute('title', value.text || '')
      el._tooltip.setContent({ '.tooltip-inner': value.text || '' })
    }
  },

  beforeUnmount(el) {
    if (el._tooltip) {
      el._tooltip.dispose()
      delete el._tooltip
    }
  },
}
