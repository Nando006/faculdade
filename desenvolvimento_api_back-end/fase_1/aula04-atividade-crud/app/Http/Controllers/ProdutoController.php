<?php

namespace App\Http\Controllers;

use App\Models\Produto;
use Illuminate\Http\Request;

class ProdutoController extends Controller
{
    /**
     * Display a listing of the resource.
     */
    public function index()
    {
        $data = Produto::with(['distribuidora', 'categoria', 'createdBy'])->get();

        return [
            'status' => 200,
            'message' => 'Produtos listados com sucesso!',
            'data' => $data
        ];
    }

    /**
     * Store a newly created resource in storage.
     */
    public function store(Request $request)
    {
        $data = Produto::create($request->all());

        return [
            'status' => 200,
            'message' => 'Produto criado com sucesso!',
            'data' => $data->load(['distribuidora', 'categoria', 'createdBy'])
        ];
    }

    /**
     * Display the specified resource.
     */
    public function show(Produto $produto)
    {
        return [
            'status' => 200,
            'message' => 'Produto criado com sucesso!',
            'data' => $produto->load(['distribuidora', 'categoria', 'createdBy']),
        ];
    }

    /**
     * Update the specified resource in storage.
     */
    public function update(Request $request, Produto $produto)
    {
        return [
            'status' => 200,
            'message' => 'Produto criado com sucesso!',
            'data' => $produto->fresh()->load(['distribuidora', 'categoria', 'createdBy'])
        ];
    }

    /**
     * Remove the specified resource from storage.
     */
    public function destroy(Produto $produto)
    {
        return [
            'status' => 200,
            'message' => 'Produto criado com sucesso!',
            'data' => $produto->delete()
        ];
    }
}
