<template>
  <div class="register">
    <h2>Регистрация</h2>
    <form @submit.prevent="registerUser" class="form-container">  <!-- Изменено на registerUser -->
      <div class="form-group">
        <label for="username">Имя пользователя:</label>
        <input v-model="username" type="text" id="username" class="form-control" required />  <!-- Исправлено на username -->
      </div>
      <div class="form-group">
        <label for="email">Email:</label>
        <input v-model="email" type="email" id="email" class="form-control" required />  <!-- Исправлено на email -->
      </div>
      <div class="form-group">
        <label for="password1">Пароль:</label>
        <input v-model="password" type="password" id="password1" class="form-control" required />  <!-- Исправлено на password -->
      </div>
      <div class="form-group">
        <label for="password2">Подтверждение пароля:</label>
        <input v-model="password2" type="password" id="password2" class="form-control" required />  <!-- Исправлено на password2 -->
      </div>
      <button type="submit" class="btn btn-primary">Зарегистрироваться</button>
    </form>
    <p v-if="error" class="error-message">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios';

export default {
  data() {
    return {
      username: '',
      email: '',
      password: '',  // Поменяно на password
      password2: '',  // Поменяно на password2
      error: null,  // Добавлена переменная для хранения ошибок
    };
  },
  methods: {
    registerUser() {  // Метод регистрации
      // Проверка на совпадение паролей
      if (this.password !== this.password2) {
        this.error = 'Пароли не совпадают';
        return;
      }

      axios.post('http://localhost:8000/funs/register/', {
        username: this.username,
        email: this.email,
        password: this.password,  // Используется password
        password2: this.password2,  // Используется password2
      })
      .then(() => {
        alert('Регистрация успешна!');
        this.error = null;
        // Здесь можно перенаправить пользователя на страницу входа
      })
      .catch(error => {
        // Проверка на существование сообщения об ошибке
        if (error.response && error.response.data) {
          this.error = error.response.data.detail || 'Ошибка регистрации';  // Используйте свойство detail или общее сообщение
        } else {
          this.error = 'Ошибка сети';
        }
      });
    }
  }
}
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

@media screen and (max-width: 768px) {
  .register {
    max-width: 90%; /* Занимает почти всю ширину экрана на мобильных устройствах */
    padding: 15px;
  }

  .form-control {
    padding: 12px;
  }

  .btn {
    padding: 12px 18px;
  }
}

@media screen and (min-width: 1024px) {
  .register {
    max-width: 600px; /* Увеличение ширины формы на десктопах */
  }

  .form-container {
    padding: 25px;
  }

  .form-control {
    padding: 15px;
  }

  .btn {
    padding: 14px 20px;
  }
}
</style>
