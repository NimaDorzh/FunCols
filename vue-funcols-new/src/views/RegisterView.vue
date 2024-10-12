<template>
  <div class="register">
    <h2>Регистрация</h2>
    <form @submit.prevent="register" class="form-container">
      <div class="form-group">
        <label for="username">Имя пользователя:</label>
        <input v-model="form.username" type="text" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input v-model="form.email" type="email" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="password1">Пароль:</label>
        <input v-model="form.password1" type="password" class="form-control" required />
      </div>
      <div class="form-group">
        <label for="password2">Подтверждение пароля:</label>
        <input v-model="form.password2" type="password" class="form-control" required />
      </div>
      <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
    </form>
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</template>

<script>
export default {
  data() {
    return {
      form: {
        username: '',
        email: '',
        password1: '',
        password2: ''
      },
      error: ''
    };
  },
  methods: {
    async register() {
      try {
        const response = await fetch('/accounts/register/', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': this.getCsrfToken()
          },
          body: JSON.stringify(this.form)
        });

        const data = await response.json();
        if (response.ok) {
          window.location.href = '/'; // Перенаправление на главную страницу
        } else {
          this.error = data.error || 'Registration failed';
        }
      } catch (error) {
        console.error('Error:', error);
        this.error = 'Что-то пошло не так.';
      }
    },
    getCsrfToken() {
      const cookieValue = document.cookie
        .split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];
      return cookieValue || '';
    }
  }
};
</script>

<style scoped>
.register {
  max-width: 400px;
  margin: 0 auto;
  padding: 20px;
  border: 1px solid #ccc;
  border-radius: 8px;
  background-color: #f9f9f9;
  box-shadow: 0px 4px 8px rgba(0, 0, 0, 0.1);
}

h2 {
  text-align: center;
  margin-bottom: 20px;
}

.form-container {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 15px;
}

.form-group label {
  font-weight: bold;
  margin-bottom: 5px;
  display: block;
}

.form-control {
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
  width: 100%;
  box-sizing: border-box;
}

.btn {
  padding: 10px 15px;
  border: none;
  border-radius: 4px;
  background-color: #007bff;
  color: #fff;
  font-size: 16px;
  cursor: pointer;
}

.btn-primary:hover {
  background-color: #0056b3;
}

.error-message {
  color: red;
  text-align: center;
  margin-top: 10px;
}
</style>
