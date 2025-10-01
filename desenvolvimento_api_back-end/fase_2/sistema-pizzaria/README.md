<p align="center"><a href="https://laravel.com" target="_blank"><img src="https://raw.githubusercontent.com/laravel/art/master/logo-lockup/5%20SVG/2%20CMYK/1%20Full%20Color/laravel-logolockup-cmyk-red.svg" width="400" alt="Laravel Logo"></a></p>

<p align="center">
<a href="https://github.com/laravel/framework/actions"><img src="https://github.com/laravel/framework/workflows/tests/badge.svg" alt="Build Status"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/dt/laravel/framework" alt="Total Downloads"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/v/laravel/framework" alt="Latest Stable Version"></a>
<a href="https://packagist.org/packages/laravel/framework"><img src="https://img.shields.io/packagist/l/laravel/framework" alt="License"></a>
</p>

## Explicação do código

1. Primeira alteração nas migration já reaproveitei a migration de users para fazer o usuário, só adicionando mas um campo chamado `role` com as opções `cliente` ou `funcionário`.

```php
$table->enum('role', [ 'cliente', 'funcionario' ])->default('cliente');
```

2. Executei o comando `php artisan make:migration create_pizzas_table` para poder gerar a migration da tabela pizza e nela adicionei os seguintes campos:

```php
$table->string('nome');
$table->enum('tamanho', [          'pequena',
'media',
'grande'
]);
$table->decimal('preco_base', 10,2);
```

3.
