import { ref } from "vue"

import { defineStore } from "pinia"

export const AuthStore = defineStore("auth", () => {
    const token = ref(localStorage.getItem(import.meta.env.VITE_ACCESS_TOKEN_KEY))
    const isAuthenticated = ref(token.value === null ? false : true)

    function setToken(value) {
        localStorage.setItem(import.meta.env.VITE_ACCESS_TOKEN_KEY, value)
        token.value = value
        isAuthenticated.value = true

    }
    function $reset() {
        localStorage.removeItem(import.meta.env.VITE_ACCESS_TOKEN_KEY)
        token.value = null
        isAuthenticated.value = false
    }

    return {
        token,
        isAuthenticated,
        setToken,
        $reset,
    }

})