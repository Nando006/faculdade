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
        Schema::create('produtos', function (Blueprint $table) {
            $table->id();
            $table->string('nome');
            $table->decimal('preco', 8, 2);
            $table->integer('quantidade');
            
            $table->foreignId('distribuidora_id')->constrained('distribuidoras', 'id')->onDelete('cascade');
            $table->foreignId('categoria_id')->constrained('categorias', 'id')->onDelete('cascade');
            $table->foreignId('created_by')->constrained('users', 'id')->onDelete('cascade');

            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('produtos');
    }
};
