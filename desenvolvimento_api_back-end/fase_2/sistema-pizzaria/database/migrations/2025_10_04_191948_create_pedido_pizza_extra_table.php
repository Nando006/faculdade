<?php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('pedido_pizza_extra', function (Blueprint $table) {
            $table->id();

            $table->foreignId('pedido_pizza_id')->constrained('pedido_pizza')->cascadeOnDelete();
            $table->foreignId('ingredient_id')->constrained('ingredientes')->cascadeOnDelete();

            $table->decimal('preco_adicional', 10,2);
            $table->unique(['pedido_pizza_id', 'ingredient_id']);

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('pedido_pizza_extra');
    }
};
