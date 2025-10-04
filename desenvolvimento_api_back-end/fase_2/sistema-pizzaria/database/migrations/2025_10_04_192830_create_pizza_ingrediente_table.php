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
        Schema::create('pizza_ingrediente', function (Blueprint $table) {
            $table->id();

            $table->foreignId('pizza_id')->constrained('pizzas')->cascadeOnDelete();
            $table->foreignId('ingrediente_id')->constrained('ingredientes')->cascadeOnDelete();

            $table->unique(['pizza_id', 'ingrediente_id']);

            
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('pizza_ingrediente');
    }
};
